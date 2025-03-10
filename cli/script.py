import click
import os
import shutil 


@click.group()
def cli():
    pass


@click.command()
@click.argument('project_name')
def create_project(project_name):
    if os.path.exists(project_name):
        click.echo(click.style(f'❌ Project {project_name} already exists.', fg='yellow'))
    else:
        os.makedirs(project_name, exist_ok=True)
        file_path = os.path.join(project_name, 'README.md')
        with open(file_path, 'w') as f:
            f.write(f'# {project_name}')
        click.echo(click.style(f'✅ Project {project_name} created!', fg='green'))


@click.command()
@click.argument('project_name')
def delete_project(project_name):
    if os.path.exists(project_name):
        shutil.rmtree(project_name)  # Recursively delete directory and its contents
        click.echo(click.style(f'✅ Project {project_name} deleted.', fg='green'))
    else:
        click.echo(click.style(f'❌ Project {project_name} does not exist.', fg='red'))


# Add commands properly
cli.add_command(create_project)
cli.add_command(delete_project)
