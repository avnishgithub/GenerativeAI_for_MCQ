from setuptools import find_packages, setup




setup(
    name='mcqgenerator',
    version='0.0.1',
    author='avnish malviya',
    author_email='avnish.malviya@gmail.com',
    install_requires = ["openai","langchain","streamlit","pytho-dotenv","pyPDF2"],
    packages=find_packages()
)