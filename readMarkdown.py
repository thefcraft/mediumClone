import markdown2
import re
import html

def extract_markdown(data):
    data = html.escape(data)
    # Define the pattern to search for
    pattern = r"```(\w*)\n([\s\S]*?)\n```"

    # Define the replacement pattern
    replacement = r'<pre><code class="\1">\2</code></pre>'

    # Perform the replacement
    modified_content = re.sub(pattern, replacement, data)

    return markdown2.markdown(modified_content)

if __name__ == '__main__':
    with open('part1.md', 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    # Convert Markdown to HTML
    html_output = extract_markdown(markdown_text)

    # Print or save the HTML output
    print(html_output)
    
    
    with open('part1.html', 'w', encoding='utf-8') as file:
        file.write(html_output)
    