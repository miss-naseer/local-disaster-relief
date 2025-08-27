# Relief Management System

## Overview
The Relief Management System is a Django-based project designed to manage disaster relief operations.  
It helps track incidents (such as floods, fires, and earthquakes), set up relief camps, register volunteers, and manage resources.  
The goal is to provide an organized way to respond to disasters and support affected communities.

## Features (Planned)
- Incident Management 
- Relief Camp Management (coming soon)
- Volunteer Management (coming soon)
- Resource Management (coming soon)
- Admin Dashboard
- REST API Endpoints for external apps

## What Has Been Accomplished So Far
- Django project setup (`relief`).
- Created `Incident` model with fields (title, description, location, severity, date, etc.).
- Implemented Django REST Framework serializers and API views for `Incident`.
- Tested CRUD operations for incidents (create, list, update, delete).
- Integrated Incident management into Django Admin for easy management.

## Challenges Faced
- Serializer field ordering in Django REST framework.
- Migration issues (no migrations applied at first).
- Remembering/handling Django superuser credentials.

**How They Were Solved:**
- Explored different serializer configurations (still pending refinement).
- Re-applied and confirmed migrations.
- Created a new superuser when the old password was forgotten.

## What’s Next
- Create and integrate the `ReliefCamp` model.
- Build `Volunteer` and `Resource` models.
- Establish relationships between incidents, camps, volunteers, and resources.
- Improve API responses and user-friendly testing.
- Finalize the Admin dashboard for all models.
