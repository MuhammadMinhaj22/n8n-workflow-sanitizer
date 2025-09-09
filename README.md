## n8n Workflow Sanitizer

This Python tool cleans and secures exported **n8n workflow JSON files** by:

- Removing credentials from nodes  
- Replacing webhook paths with a safe default (`my-webhook`)  
- Masking all `id` fields with a placeholder  
- Replacing UUIDs with a safe placeholder  

### Usage
1. Run the script:
   ```bash
   python sanitize.py
