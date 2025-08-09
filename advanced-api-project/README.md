A Django REST Framework API for managing books with role-based permissions.

---

## **Endpoints and Permissions**

| Endpoint                              | Method | Description                          | Permissions |
|---------------------------------------|--------|--------------------------------------|-------------|
| `/books/`                             | GET    | List all books                       | Public      |
| `/books/<id>/`                        | GET    | Retrieve a single book               | Public      |
| `/books/create/`                      | POST   | Create a new book                    | Authenticated users |
| `/books/<id>/update/`                 | PUT/PATCH | Update an existing book          | Owner only  |
| `/books/<id>/delete/`                 | DELETE | Delete a book                        | Admin only  |
| `/login/`                             | POST   | Get authentication token             | Public (provide username & password) |

---

## **Permissions Applied**

- **Public Access**: Anyone can view books (list and detail).
- **Authenticated Users**: Can create books.
- **Owner Only**: Can update their own books.
- **Admin Only**: Can delete books.

---

## **Example Requests & Responses**

## Filtering, Searching, and Ordering

### Filtering
Filter books by title, author, or publication_year:

### Searching
Search books by title or author:

### Ordering
Order books by title or publication_year:


### **1. Create a Book (Authenticated User)**
**Request:**
```bash
POST /books/create/
Authorization: Token your_token
Content-Type: application/json

{
    "title": "The Alchemist",
    "author": "Paulo Coelho"
}
Response:

json

{
    "id": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "owner": "admin"
}
2. Update a Book (Owner)
Request:

PATCH /books/1/update/
Authorization: Token your_token
Content-Type: application/json

{
    "title": "The Alchemist - Updated"
}
Response:

json

{
    "id": 1,
    "title": "The Alchemist - Updated",
    "author": "Paulo Coelho",
    "owner": "admin"
}
3. Delete a Book (Admin)
Request:


DELETE /books/1/delete/
Authorization: Token admin_token
Response:

json
{
    "detail": "Book deleted successfully"
}
Authentication
We use Token Authentication.
To get a token:


POST /login/
Content-Type: application/json

{
    "username": "admin",
    "password": "password123"
}
Response:

json

{
    "token": "94d6f67a019b5a..."
}


---

If you want, in **Step 7** we can make the `README.md` even stronger by adding an **API usage flowchart** so it’s visually clear how permissions work.  

Do you want me to prepare that flowchart next?