#!/bin/bash

path=/home/sortbito/dev/public-projects/venex

cd $path

uv run -m app.jobs.binance_job
