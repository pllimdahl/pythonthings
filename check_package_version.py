import subprocess

def check_package_version(package_name):
    try:
        # Use the dpkg-query command to get the package version
        result = subprocess.run(['dpkg-query', '--show', '--showformat=${Version}', package_name],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        package_version = result.stdout.strip()
        return package_version
    except subprocess.CalledProcessError as e:
        # Handle the case when the package is not installed
        return f"Package '{package_name}' not installed"

if __name__ == "__main__":
    package_name = "bash"  # Replace with the package name you want to check
    version = check_package_version(package_name)
    print(f"Version of {package_name}: {version}")
