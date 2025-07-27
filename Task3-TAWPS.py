import os
import shutil
import re
import requests
from datetime import datetime

def file_organizer():
    """
    Task 1: Move .jpg files from source folder to destination folder
    Automates organizing image files
    """
    print("="*50)
    print("         FILE ORGANIZER - JPG MOVER")
    print("="*50)
    
    # Get source and destination folders from user
    source_folder = input("Enter source folder path (or press Enter for current directory): ").strip()
    if not source_folder:
        source_folder = "."
    
    # Create destination folder name
    destination_folder = input("Enter destination folder name (default: 'organized_images'): ").strip()
    if not destination_folder:
        destination_folder = "organized_images"
    
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist!")
        return
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")
    
    # Find all .jpg files (including .jpeg)
    jpg_files = []
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            jpg_files.append(filename)
    
    if not jpg_files:
        print("No .jpg files found in the source folder!")
        return
    
    print(f"\nFound {len(jpg_files)} JPG files:")
    for i, filename in enumerate(jpg_files, 1):
        print(f"  {i}. {filename}")
    
    # Ask for confirmation
    confirm = input(f"\nMove all {len(jpg_files)} files to '{destination_folder}'? (y/n): ").lower()
    
    if confirm in ['y', 'yes']:
        moved_count = 0
        failed_count = 0
        
        for filename in jpg_files:
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            
            try:
                # Handle file name conflicts
                if os.path.exists(dest_path):
                    name, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_filename = f"{name}_{counter}{ext}"
                        dest_path = os.path.join(destination_folder, new_filename)
                        counter += 1
                    print(f"  Renamed '{filename}' to '{os.path.basename(dest_path)}'")
                
                shutil.move(source_path, dest_path)
                moved_count += 1
                print(f"  ✓ Moved: {filename}")
                
            except Exception as e:
                print(f"  ✗ Failed to move {filename}: {e}")
                failed_count += 1
        
        print(f"\n📁 Task completed!")
        print(f"   Successfully moved: {moved_count} files")
        if failed_count > 0:
            print(f"   Failed to move: {failed_count} files")
    else:
        print("Operation cancelled.")

def email_extractor():
    """
    Task 2: Extract email addresses from a text file and save to another file
    Automates extracting emails from documents, logs, etc.
    """
    print("="*50)
    print("         EMAIL EXTRACTOR")
    print("="*50)
    
    # Get input file from user
    input_file = input("Enter path to text file (or press Enter for 'sample_text.txt'): ").strip()
    if not input_file:
        input_file = "sample_text.txt"
        # Create a sample file if it doesn't exist
        if not os.path.exists(input_file):
            sample_content = """
            Contact us at support@company.com for help.
            You can also reach John at john.doe@email.com or 
            Mary at mary.smith@example.org for more information.
            Invalid emails: notanemail, @invalid.com, user@.com
            More contacts: admin@website.net, info@business.co.uk
            """
            with open(input_file, 'w') as f:
                f.write(sample_content)
            print(f"Created sample file: {input_file}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist!")
        return
    
    try:
        # Read the file content
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regular expression pattern for email addresses
        # This pattern matches most common email formats
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Find all email addresses
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates while preserving order
        unique_emails = list(dict.fromkeys(emails))
        
        if not unique_emails:
            print("No email addresses found in the file!")
            return
        
        print(f"\nFound {len(unique_emails)} unique email addresses:")
        for i, email in enumerate(unique_emails, 1):
            print(f"  {i}. {email}")
        
        # Ask for output file name
        output_file = input("\nEnter output filename (default: 'extracted_emails.txt'): ").strip()
        if not output_file:
            output_file = "extracted_emails.txt"
        
        # Save emails to output file
        with open(output_file, 'w') as file:
            file.write(f"Email Addresses Extracted from: {input_file}\n")
            file.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Total Found: {len(unique_emails)}\n")
            file.write("=" * 50 + "\n\n")
            
            for i, email in enumerate(unique_emails, 1):
                file.write(f"{i}. {email}\n")
        
        print(f"\n📧 Emails successfully extracted and saved to '{output_file}'!")
        
    except Exception as e:
        print(f"Error processing file: {e}")

def webpage_scraper():
    """
    Task 3: Scrape the title of a webpage and save it to a file
    Automates collecting information from websites
    """
    print("="*50)
    print("         WEBPAGE TITLE SCRAPER")
    print("="*50)
    
    # Default URLs to choose from
    default_urls = [
        "https://httpbin.org/html",  # Simple test page
        "https://example.com",       # Basic example site
        "https://python.org",        # Python official site
        "https://github.com",        # GitHub
        "https://stackoverflow.com"  # Stack Overflow
    ]
    
    print("Choose an option:")
    print("1. Use a predefined URL")
    print("2. Enter a custom URL")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        print("\nPredefined URLs:")
        for i, url in enumerate(default_urls, 1):
            print(f"  {i}. {url}")
        
        try:
            url_choice = int(input("\nSelect URL (1-5): ")) - 1
            if 0 <= url_choice < len(default_urls):
                url = default_urls[url_choice]
            else:
                print("Invalid choice. Using default URL.")
                url = default_urls[0]
        except ValueError:
            print("Invalid input. Using default URL.")
            url = default_urls[0]
    
    elif choice == "2":
        url = input("Enter the webpage URL: ").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
    else:
        print("Invalid choice. Using default URL.")
        url = default_urls[0]
    
    print(f"\nScraping title from: {url}")
    
    try:
        # Send HTTP request with headers to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Extract title using regex
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, response.text, re.IGNORECASE | re.DOTALL)
        
        if title_match:
            title = title_match.group(1).strip()
            # Clean up the title (remove extra whitespace and decode HTML entities)
            title = re.sub(r'\s+', ' ', title)
            
            print(f"\n🎯 Page Title Found: '{title}'")
            
            # Ask for output file name
            output_file = input("\nEnter output filename (default: 'scraped_titles.txt'): ").strip()
            if not output_file:
                output_file = "scraped_titles.txt"
            
            # Check if file exists to determine if we should append
            file_exists = os.path.exists(output_file)
            mode = 'a' if file_exists else 'w'
            
            # Save title to file
            with open(output_file, mode, encoding='utf-8') as file:
                if not file_exists:
                    file.write("WEBPAGE TITLE SCRAPING LOG\n")
                    file.write("=" * 40 + "\n\n")
                
                file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"URL: {url}\n")
                file.write(f"Title: {title}\n")
                file.write("-" * 40 + "\n\n")
            
            print(f"📄 Title saved to '{output_file}'!")
            
        else:
            print("❌ No title found on this webpage!")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing webpage: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main menu to choose which automation task to run"""
    while True:
        print("\n" + "="*60)
        print("           PYTHON TASK AUTOMATION SUITE")
        print("="*60)
        print("Choose an automation task:")
        print("1. 📁 File Organizer - Move JPG files to organized folder")
        print("2. 📧 Email Extractor - Extract emails from text files")
        print("3. 🌐 Webpage Scraper - Scrape webpage titles")
        print("4. ❌ Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            file_organizer()
        elif choice == "2":
            email_extractor()
        elif choice == "3":
            webpage_scraper()
        elif choice == "4":
            print("Thank you for using Python Task Automation Suite! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
