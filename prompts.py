PROMPTS = {
    "Handwritten Notes": """
    Convert these handwritten notes into clean typed notes.

    Keep:
    - Headings
    - Bullet points
    - Important keywords

    Format nicely in Markdown.
    """,

    "Business Card": """
    Extract the following information:

    - Name
    - Company
    - Phone
    - Email
    - Website
    - Address

    Return clean JSON format.
    """,

    "Receipt": """
    Extract all receipt information.

    Return as markdown table:

    | Item | Quantity | Price |

    Also calculate total amount.
    """,

    "Whiteboard": """
    Convert this whiteboard image into structured notes.

    Create:
    - Title
    - Main Points
    - Action Items
    - Summary

    Use markdown formatting.
    """
}