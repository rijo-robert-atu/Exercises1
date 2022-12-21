#!/bin/bash
# by: Rijo
# Date: 21DEC22
# Function: Perform a commit to GIT
# Script: AddCommitPush.sh
clear
git status
echo '**************************************************'
echo "Performing an add for all files in this directory"
git add .
git status
echo '**************************************************'
echo 'Enter the commit message:'
read CommitMessage
git commit -m "$CommitMessage"
git status
echo '**************************************************'
echo 'Pushing to GITHUB repository'
git push -u origin master
echo '**************************************************'
echo 'Done!'