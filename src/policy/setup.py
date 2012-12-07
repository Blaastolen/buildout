from setuptools import setup


setup(name='policy',
    version='1.0dev',
    url='http://localhost',
    license='Private',
    description='Policy',
    author='Jarn AS',
    author_email='info@jarn.com',
    long_description='',
    packages=['policy'],
    install_requires=[
        'setuptools',
        'Plone',
        'plone.app.testing',
        'Pillow',
        'Products.PloneFormGen',
        'plone.app.dexterity',
        'diazotheme.bootstrap',
        'collective.contentleadimage',
        'collective.portletpage',
        'collective.carousel',
        'z3c.jbot',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
    },
)
