#!/bin/bash

path=/home/sortbito/dev/public-projects/venex

cd $path

uv run -m app.services.jobs.binance_job
