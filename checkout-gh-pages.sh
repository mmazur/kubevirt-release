#!/bin/bash
set -ex
rm -rf gh-pages
mkdir gh-pages
cp -a .git gh-pages
cd gh-pages
git fetch origin +gh-pages:gh-pages
git checkout gh-pages
