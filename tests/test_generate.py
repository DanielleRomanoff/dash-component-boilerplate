import json


default_context = {
    'install_dependencies': False,
    'project_name': 'Test Component',
    'author_name': 'test',
    'author_email': 'test@example.com'
}


def test_package_json(cookies):
    result = cookies.bake(extra_context=default_context)

    package_json = json.loads(result.project.join('package.json').read())

    assert package_json['name'] == 'test_component'
    assert package_json['license'] == 'MIT'
    assert package_json['author'] == \
        '{} {}'.format(default_context['author_name'],
                       default_context['author_email'])
