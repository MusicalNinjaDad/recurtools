#!/bin/bash
nohup bash -c 'mkdocs serve &' >> docs/serve.out 2>> docs/serve.err
