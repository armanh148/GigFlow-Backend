from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from items.models import Item

class Command(BaseCommand):
    help = 'Seeds initial sample records into database and creates Django admin superuser'

    def handle(self, *args, **options):
        # Create Superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superuser "admin" (password: "admin") created successfully.'))
        else:
            self.stdout.write('Superuser "admin" already exists.')

        # Seed Items
        Item.objects.all().delete()

        initial_items = [
            {
                'title': 'E-Commerce Checkout Redesign',
                'description': 'Upgrade the UI/UX checkout workflow with express multi-payment options and live validation.',
                'category': 'Product',
                'status': 'In Progress',
                'priority': 'High',
                'price': 1250.00,
            },
            {
                'title': 'API Authentication Service',
                'description': 'Implement JWT authentication, refresh token rotation, and RBAC middleware.',
                'category': 'Feature',
                'status': 'Completed',
                'priority': 'Urgent',
                'price': 850.00,
            },
            {
                'title': 'Fix Safari Mobile Modal Animation Glitch',
                'description': 'Resolve backdrop blur rendering artifacts when opening modals on iOS Safari 17.',
                'category': 'Bug',
                'status': 'Pending',
                'priority': 'Medium',
                'price': 150.00,
            },
            {
                'title': 'Automated CI/CD Pipeline Setup',
                'description': 'Configure GitHub Actions for automated unit testing, linting, and Docker container build.',
                'category': 'Task',
                'status': 'Completed',
                'priority': 'Medium',
                'price': 450.00,
            },
            {
                'title': 'Analytics Dashboard Widget',
                'description': 'Create real-time revenue and task completion charts using Recharts library.',
                'category': 'Product',
                'status': 'In Progress',
                'priority': 'High',
                'price': 980.00,
            },
            {
                'title': 'Database Indexing & Query Optimization',
                'description': 'Add composite indexes on frequently filtered item category and status columns.',
                'category': 'Task',
                'status': 'Pending',
                'priority': 'Low',
                'price': 300.00,
            }
        ]

        for data in initial_items:
            Item.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(initial_items)} items into Django SQLite database.'))
