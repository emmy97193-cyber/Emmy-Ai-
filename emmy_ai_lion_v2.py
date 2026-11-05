# NAME: EMMY★..★
# CODE: EMMY-AI-LION-V2-001
# FILE: emmy_ai_lion_v2.py

import bpy
import math
from mathutils import Vector

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 64
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.frame_start = 1
scene.frame_end = 180
scene.render.fps = 24

def material(name, color, metallic=0,
             roughness=0.4, emission=None,
             strength=0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get(
        "Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (
        *color, 1)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    if emission:
        bsdf.inputs["Emission Color"].default_value = (
            *emission, 1)
        bsdf.inputs["Emission Strength"].default_value = strength
    return mat

gold = material("Royal Golden Fur",
    (0.65, 0.27, 0.045), 0.35, 0.32)
skin = material("Lion Face",
    (0.55, 0.25, 0.08), 0, 0.5)
dark = material("Dark Details",
    (0.035, 0.018, 0.012))
black = material("Nose and Mouth",
    (0.012, 0.008, 0.006))
white = material("Eye Whites",
    (0.9, 0.8, 0.55))
green = material("AI Neon Green",
    (0.01, 0.8, 0.2), 0.35, 0.2,
    (0.0, 1.0, 0.3), 4)
chest_mat = material("AI Chest Core",
    (0.01, 0.2, 0.08), 0.6, 0.2,
    (0.0, 1.0, 0.3), 3)

def sphere(name, location, scale, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=32, ring_count=20,
        location=location)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.shade_smooth()
    if mat:
        obj.data.materials.append(mat)
    return obj

def cone_between(name, start, end, radius, mat):
    start, end = Vector(start), Vector(end)
    direction = end - start
    bpy.ops.mesh.primitive_cone_add(
        vertices=12, radius1=radius,
        radius2=0.025,
        depth=direction.length,
        location=(start + end) / 2)
    obj = bpy.context.active_object
    obj.name = name
    obj.rotation_mode = 'QUATERNION'
    obj.rotation_quaternion = direction.to_track_quat('Z', 'Y')
    obj.data.materials.append(mat)
    return obj

def key_loc(obj, frame, loc):
    obj.location = loc
    obj.keyframe_insert(
        data_path="location", frame=frame)

def key_rot(obj, frame, rot):
    obj.rotation_euler = rot
    obj.keyframe_insert(
        data_path="rotation_euler", frame=frame)

body = sphere("Lion Body",
    (0, 0, 1.65), (1.35, 0.55, 0.65), gold)
chest = sphere("Lion Chest",
    (0.9, 0, 1.8), (0.55, 0.65, 0.8), gold)
chest_core = sphere("Chest Core",
    (1.35, 0, 1.85), (0.18, 0.18, 0.18), chest_mat)

legs = []
for x in [-0.85, 0.85]:
    for y in [-0.36, 0.36]:
        leg = sphere("Lion Leg",
            (x, y, 0.8), (0.25, 0.25, 0.65), gold)
        paw = sphere("Lion Paw",
            (x + 0.08, y, 0.25),
            (0.32, 0.28, 0.18), skin)
        legs.append(leg)

tail = cone_between("Lion Tail",
    (-1.1, 0, 1.8), (-2.0, 0, 2.3),
    0.10, gold)
sphere("Tail Tuft",
    (-2.08, 0, 2.38),
    (0.18, 0.16, 0.25), dark)

head_group = bpy.data.objects.new(
    "Head Group", None)
scene.collection.objects.link(head_group)
head_group.location = (1.15, 0, 2.55)

mane_base = sphere("Mane Base",
    (1.15, 0, 2.55), (0.95, 0.78, 1.0), gold)
head = sphere("Lion Face",
    (1.55, 0, 2.65), (0.66, 0.53, 0.72), skin)
head.parent = head_group

for side in [-1, 1]:
    ear = sphere("Lion Ear",
        (1.12, side*0.48, 3.13),
        (0.23, 0.16, 0.25), dark)
    ear.parent = head_group
    eye = sphere("AI Glowing Eye",
        (1.88, side*0.475, 2.85),
        (0.11, 0.06, 0.08), green)
    eye.parent = head_group

upper_muzzle = sphere("Upper Muzzle",
    (2.05, 0, 2.45), (0.28, 0.30, 0.26), gold)
upper_muzzle.parent = head_group
nose = sphere("Lion Nose",
    (2.25, 0, 2.55), (0.12, 0.14, 0.10), black)
nose.parent = head_group
jaw = sphere("Lower Jaw",
    (2.0, 0, 2.15), (0.26, 0.26, 0.18), skin)
jaw.parent = head_group
jaw.rotation_mode = 'XYZ'

for i in range(4):
    tooth = sphere(f"Tooth_{i}",
        (2.15 + (i-1.5)*0.08,
         -0.12 + (i%2)*0.24, 2.28),
        (0.03, 0.03, 0.07), white)
    tooth.parent = jaw

bpy.ops.mesh.primitive_uv_sphere_add(
    radius=0.95, segments=32, ring_count=16,
    location=(1.15, 0, 2.55))
mane_mesh = bpy.context.active_object
mane_mesh.name = "Mane Hair Emitter"
mane_mesh.data.materials.append(gold)
bpy.ops.object.modifier_add(type='PARTICLE_SYSTEM')
psys = mane_mesh.particle_systems.active.settings
psys.type = 'HAIR'
psys.count = 2500
psys.hair_length = 0.55
psys.emit_from = 'FACE'
psys.use_emit_random = True
psys.child_type = 'INTERPOLATED'
psys.child_nbr = 20
psys.kink_type = 'CURL'
psys.kink_amplitude = 0.15
psys.kink_frequency = 2.0

for frame, rot_x in [(1, 0), (40, 0.05),
    (55, 0.55), (70, 0.05), (110, 0.05),
    (125, 0.6), (140, 0), (180, 0)]:
    key_rot(jaw, frame, (rot_x, 0, 0))

for frame, z in [(1, 2.55), (55, 2.65),
    (70, 2.55), (125, 2.68), (140, 2.55)]:
    key_loc(head_group, frame, (1.15, 0, z))

for i, leg in enumerate(legs):
    offset = (i % 2) * 15
    for f in range(1, 181, 15):
        phase = math.sin((f + offset) * 0.15)
        key_loc(leg, f, (leg.location.x,
            leg.location.y,
            0.8 + max(0, phase)*0.25))

chest_bsdf = chest_mat.node_tree.nodes.get(
    "Principled BSDF")
for frame, strength in [(1, 3), (30, 6),
    (60, 3), (90, 7), (120, 3),
    (150, 6), (180, 3)]:
    chest_bsdf.inputs["Emission Strength"].default_value = strength
    chest_bsdf.inputs["Emission Strength"].keyframe_insert(
        data_path="default_value", frame=frame)

bpy.ops.object.camera_add(
    location=(6, -6, 3.5),
    rotation=(1.1, 0, 0.7))
cam = bpy.context.active_object
scene.camera = cam
key_loc(cam, 1, (7, -7, 4.5))
key_loc(cam, 60, (5, -4.5, 3.0))
key_loc(cam, 180, (4.2, -3.2, 2.8))
key_rot(cam, 1, (1.1, 0, 0.8))
key_rot(cam, 180, (1.35, 0, 0.6))

bpy.ops.object.light_add(type='SUN',
    location=(5, -5, 8))
sun = bpy.context.active_object
sun.data.energy = 3
bpy.ops.object.light_add(type='POINT',
    location=(1.5, 0, 2.5))
glow = bpy.context.active_object
glow.data.color = (0, 1, 0.3)
glow.data.energy = 500

print("EMMY AI LION V2 READY")
