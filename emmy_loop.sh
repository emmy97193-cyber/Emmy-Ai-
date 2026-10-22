echo 'export DISCORD_BOT_TOKEN="your_token_here"' >> ~/.bashrc
echo 'export CHANNEL_ID="your_channel_id"' >> ~/.bashrc
source ~/.bashrc
chmod +x emmy_loop.sh
./emmy_loop.sh 60
