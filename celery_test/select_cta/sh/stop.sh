#!/usr/bin/env bash

PROCESS_NAME="celery"

# kill celery process
PROCESS=`ps -ef | grep $PROCESS_NAME | grep -v grep | grep -v PPID | awk '{ print $2}'`

for i in $PROCESS
do
  echo "Kill the $1 process [ $i ]"
  kill -9 $i
done

# kill celery process
PROCESS=`ps -ef | grep main_shell | grep -v grep | grep -v PPID | awk '{ print $2}'`

for i in $PROCESS
do
  echo "Kill the $1 process [ $i ]"
  kill -9 $i
done
