import subprocess

class StartupService:
    def __init__(self, rpm_repos:dict, flatpak_repos:dict):
        self.rpm_repos = rpm_repos
        self.flatpak_repos = flatpak_repos

    def repo_check(self):
        for repo, url in self.rpm_repos.items():
            check_result = subprocess.run(f"dnf repolist | grep -wo {repo}", shell=True, capture_output=True)
            if repo not in check_result.stdout.decode():
                print(f"{repo} not enabled")
                subprocess.run(f"pkexec dnf install -y {url}", shell=True)
                self.repo_check()

        for repo, url in self.flatpak_repos.items():
            check_result = subprocess.run(f"flatpak remotes | grep -wo {repo}", shell=True, capture_output=True)
            if repo not in check_result.stdout.decode():
                print(f"{repo} not enabled")
                subprocess.run(f"flatpak remote-add --if-not-exists {repo} {url}", shell=True)
                self.repo_check()