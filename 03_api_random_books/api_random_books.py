import requests


def main(url):
    try:
        response = requests.get(url)
        data = response.json()
        if data["data"] and "success" in data:
            for book in data["data"]["data"]:
                book_id = book.get("id", "N/A")
                title = book["volumeInfo"].get("title", "N/A")
                categories = book["volumeInfo"].get("categories", ["N/A"])
                authors = book["volumeInfo"].get("authors", ["N/A"])

                print(
                    f"ID: {book_id}, Title: {title}, Categories: {', '.join(categories)}, Authors: {', '.join(authors)}"
                )
                print("*" * 100)
        else:
            print("Something went wrong while getting the data")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
    main(url)
