# IPTV Streaming Web Application

## Overview

This is a Flask-based IPTV streaming web application that allows users to manage and stream HLS (.m3u8) video channels. The application provides a public interface for viewing available channels and an admin panel for managing channel content. It features embedded video players suitable for Discord Activities and iframe integration, with support for categorized channel organization and public/private channel visibility controls.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Web Framework
- **Flask**: Core web framework with modular blueprint architecture
- **Blueprint Structure**: Separate modules for authentication (`auth.py`) and channel management (`channels.py`)
- **Template Engine**: Jinja2 templates with base template inheritance

### Authentication & Authorization
- **Flask-Login**: Session-based user authentication
- **Password Security**: BCrypt for password hashing
- **Role-Based Access**: Admin-only decorator for protected routes
- **User Model**: Simple user system with admin flag

### Database Layer
- **SQLAlchemy ORM**: Database abstraction layer
- **Models**: User and Channel entities with relationships
- **Migration Strategy**: Manual database initialization via `create_admin.py`
- **Default Database**: SQLite for development (configurable via environment)

### Frontend Architecture
- **Static Assets**: Custom CSS with dark theme and responsive grid layout
- **Video Player**: Native HTML5 video elements with HLS support
- **JavaScript**: Minimal client-side code for error handling
- **Responsive Design**: Grid-based layout for channel cards

### Channel Management
- **CRUD Operations**: Full channel lifecycle management (create, read, update, delete)
- **Visibility Control**: Public/private channel flags
- **Categorization**: Optional category system for channel organization
- **URL Storage**: Direct HLS stream URL storage

### Embed System
- **Dedicated Embed Route**: Separate lightweight player for iframe integration
- **Discord Activity Support**: Optimized for Discord embedded applications
- **Cross-Origin Compatibility**: Designed for iframe embedding

## External Dependencies

### Python Packages
- **Flask 3.0.3**: Web framework
- **Flask-SQLAlchemy 3.1.1**: ORM and database integration
- **Flask-Login**: User session management
- **Flask-Bcrypt 1.0.1**: Password hashing
- **python-dotenv 1.0.1**: Environment variable management

### Database
- **SQLite**: Default local database (production can use PostgreSQL via DATABASE_URL)
- **No migrations framework**: Manual schema management

### Media Streaming
- **HLS Protocol**: HTTP Live Streaming (.m3u8) support
- **Native Browser Support**: Relies on browser's built-in HLS capabilities
- **No CDN Integration**: Direct URL streaming without content delivery network

### Configuration
- **Environment Variables**: SECRET_KEY and DATABASE_URL configuration
- **Development Defaults**: SQLite and basic secret key for local development