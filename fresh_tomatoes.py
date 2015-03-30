import webbrowser
import os
import re

# Load head HTML template
head_template = open('templates/head_template.html', 'r')
# Load content HTML template
content_template = open('templates/content_template.html', 'r')
# Load movie HTML tile
tile_template = open('templates/movie_tile.html', 'r')

# Styles and scripting for the page
main_page_head = head_template.read();
# The main page layout and title bar
main_page_content = content_template.read();
# A single movie entry html template
movie_tile_content = tile_template.read();

# Close files
head_template.close()
content_template.close()
tile_template.close()


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(
            0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            overview=movie.storyline,
            tagline=movie.tagline,
            genre_1=movie.genres[0],
            release_date=movie.release_date,
            runtime=movie.runtime,
            rating=movie.rating,
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically
    # generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
