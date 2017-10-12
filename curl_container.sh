#!/bin/bash
for ((i=1;i<5;i++));
do
    curl -s localhost:500${i};
done

