// src/main.rs
use anyhow::Result;
use pdf::file::{File, Page};
use serde_json::Value;

#[derive(Debug)]
struct PdfProcessor {}

impl PdfProcessor {
    pub fn extract_text(&self, pdf_bytes: Vec<u8>) -> Result<Value> {
        let pdf = File::from_data(&pdf_bytes)?;
        let mut pages = Vec::new();
        
        for page in pdf.pages() {
            let text = page.get_text()?;
            pages.push(text);
        }
        
        Ok(json!({
            "pages": pdf.pages().len(),
            "content": pages
        }))
    }
}