# LibraryProject

A basic Django project created for development environment setup practice.

## Permissions and Groups Setup

This app uses Django's built-in permissions and groups system.

### Custom Permissions on `Article` Model:
- `can_view` — View articles
- `can_create` — Create new articles
- `can_edit` — Edit existing articles
- `can_delete` — Delete articles

### Groups:
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

### Views Enforcing Permissions:
- `/articles/`: Requires `can_view`
- `/articles/create/`: Requires `can_create`
- `/articles/edit/<id>/`: Requires `can_edit`
- `/articles/delete/<id>/`: Requires `can_delete`

Assign users to groups through Django Admin or scripts in `management/commands/`.