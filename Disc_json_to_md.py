import json
import os
import re
from datetime import datetime
from markdownify import markdownify as md # <--- Import the library

# Folder containing your JSON files
folder_path = 'Discourse_json'

# Iterate through all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        # Extract post number from the last 6 digits of the filename
        post_number = filename[-11:-5]  # Extracts '161071' from 'topic_161071.json'
        
        # Build the full file path
        file_path = os.path.join(folder_path, filename)

        def clean_html(content):
            """
            Converts HTML content to clean Markdown using the markdownify library.
            """
            # The 'heading_style="ATX"' option ensures <h1> becomes #, <h2> becomes ##
            # strip_tags removes any tags that markdownify doesn't know how to convert
            # This is great for getting rid of <svg>, custom <span> tags, etc.
            return md(content, heading_style="ATX", strip=['svg', 'div', 'span']).strip()

        # --- Your original code continues below ---

        try:
            # Load the JSON file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Extract topic title and details
            topic_title = data.get('title', 'No Title')
            topic_slug = data.get('slug', 'no-slug')
            created_at = data.get('created_at', 'N/A')
            created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%B %d, %Y %H:%M:%S')

            # Start the markdown content with post number and title
            markdown_content = f"# Post No: {post_number}\n"
            markdown_content += f"# {topic_title}\n"
            markdown_content += f"**Topic Slug**: {topic_slug}\n"
            markdown_content += f"**Created At**: {created_at}\n\n"

            # Extract posts and convert them to markdown
            for post in data['post_stream']['posts']:
                post_id = post.get('id')
                user_name = post.get('name')
                created_at_post = post.get('created_at') # Use a different variable name
                content = post.get('cooked', '')
                
                # Clean HTML tags from post content
                clean_content = clean_html(content)

                # Format the timestamp
                formatted_created_at = datetime.strptime(created_at_post, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%B %d, %Y %H:%M:%S')

                # Add markdown for this post
                markdown_content += f"## Post by {user_name} - {formatted_created_at}\n"
                markdown_content += f"**Post ID**: {post_id}\n\n"
                markdown_content += f"{clean_content}\n\n"
                
                # Add a link to the post
                post_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_slug}/{post_id}"
                markdown_content += f"[Link to Post]({post_url})\n\n"
                markdown_content += "---\n\n" # Add a horizontal rule for better separation

            # Add suggested topics (optional)
            if 'suggested_topics' in data:
                markdown_content += "## Suggested Topics\n"
                for topic in data.get('suggested_topics', []):
                    suggested_title = topic.get('title')
                    suggested_slug = topic.get('slug')
                    # Note: The base URL for suggested topics might be different. Adjust if needed.
                    suggested_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{suggested_slug}"
                    markdown_content += f"- [{suggested_title}]({suggested_url})\n"

            # Save the markdown content to a file named with the post number
            output_path = f"discourse_topic_{post_number}.md"
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(markdown_content)

            print(f"Markdown file '{output_path}' created successfully.")

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing file {post_number}: {e}")