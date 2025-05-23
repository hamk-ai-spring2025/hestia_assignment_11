# To run this code you need to install the following dependencies:
# pip install google-genai markdown-pdf python-dotenv

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from markdown_pdf import MarkdownPdf, Section


def generate_essay():
    """
    Prompt the user for a research question, generate an essay using Gemini API,
    and save the result as a PDF. Use APA-7 style for citations and references.
    """
    # Load environment variables from a .env file
    load_dotenv()
    
    # Initialize Gemini client
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    # Get user input for the research question
    user_question = input("Enter your research question: ")
    
    # Configure the model and request
    model = "gemini-2.5-flash-preview-05-20"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_question),
            ],
        ),
    ]
    
    tools = [
        types.Tool(url_context=types.UrlContext()),
        types.Tool(google_search=types.GoogleSearch()),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature=0.9,
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a research assistant bot. You access relevant academic, valid information sources and databases, to provide conclusive and detailed answers to the users research questions. You provide your output in markdown format essays, including the standard academic structure of abstract, introduction, theory, analysis, conclusions and discussion, with a reference list at the end. Use APA-7 style for in-text citations and final references."""),
        ],
    )

    # Generate the essay content
    print("Generating essay...")
    essay_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        chunk_text = chunk.text
        essay_text += chunk_text
        print(chunk_text, end="")
    
    # Create and save PDF
    print("\n\nSaving PDF...")
    
    # Create a title from the user question
    title = user_question
    if len(title) > 50:
        title = title[:47] + "..."
    
    # Generate PDF
    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(essay_text, paper_size="A4"), user_css="table, td, th {border: 1px solid black;}")
    pdf.meta["title"] = title
    pdf.meta["author"] = "Generated by Gemini AI"
    
    # Save PDF with a sensible filename
    filename = "essay_" + "".join(c if c.isalnum() else "_" for c in title[:30]) + ".pdf"
    pdf.save(filename)
    
    print(f"\nEssay saved as {filename}")


if __name__ == "__main__":
    generate_essay()