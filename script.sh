#!/bin/bash

QUERY_FILE="CBX3.fasta"
PROTEOMES_DIR="/mnt/storage/project_2023/proteomes/"
current_dir=$(pwd)

cd "$PROTEOMES_DIR"

for file in *.faa; do
  filename=$(basename "$file" .faa)
  blastp -query "$current_dir/$QUERY_FILE" -db "$PROTEOMES_DIR/$file" -out "$current_dir/$filename.blast" -outfmt 7
done