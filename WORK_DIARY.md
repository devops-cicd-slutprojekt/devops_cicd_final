# Team name
### Gagman

## Team members
- Erik Gagner
- Christoffer Forsman

## Work Diary

### Day 1
Spent all day "pair-programming"
- Decided on using GitLab Flow.
- Laid the groundwork for future testing (Cov, Lint)
- Created and tested first implementation of github actions
- Docker ghcr tag/image created and pushed manually
- Kubernetes pod manually pulled from docker image (ghcr.io) and deployed as a service


### Day 2
Pair-programming
- Implemented pre-commit testing with pylint


### Day 3
Pair-programming
- GitHub Action now tags, builds and pushes docker container to ghcr. Tags container with 'latest' if main branch
- Display coverage in runner terminal
- Pre-commit now runs unit-tests
