#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get install -y nginx
sudo service nginx start

sudo mkdir -p "/data/"
sudo mkdir -p "/data/web_static/"
sudo mkdir -p "/data/web_static/releases/"
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"
sudo touch "/data/web_static/releases/test/index.html"
sudo echo "some simple data" | sudo tee "/data/web_static/releases/test/index.html"

target="/data/web_static/current"
link_name="/data/web_static/releases/test/"
sudo ln -sf "$link_name" "$target"
data="/data/"
sudo chown -R ubuntu:ubuntu "$data"
config="/etc/nginx/sites-enabled/default"
sudo sed -i "38i \\\\tlocation /hbnb_static/ {\n\t\talias $target/;\n\t\tautoindex off;\n\t}\n" "$config"
sudo service nginx restart
