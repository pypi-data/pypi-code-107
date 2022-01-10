from setuptools import setup, find_packages
packages = ["web_agent"]
#python setup.py sdist upload  
#python setup.py bdist_wheel

setup(
    name = 'web_agent',
    version = '1.1.1',
    keywords = ['runner', 'server'],
    description = 'NVMe production server',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
      ],
    license = 'MIT License',
	url = 'https://pypi.org/project/web_agent',
    install_requires = ['flask',
						'flask-restful',
						'requests',
						'PyMySQL==1.0.2',
						'pyftpdlib',
						'nose',
						'nose-printlog',
                        'checksumdir',
                        'pyyaml'],
    packages = find_packages(),
    include_package_data=True, 
    author = 'yuwen123441',
    author_email = 'yuwen123441@126.com',
    platforms = 'any',
    entry_points = {
        'console_scripts': [
        'agent = web_agent.run:run'
        ]}
)