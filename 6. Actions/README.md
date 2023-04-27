# LAB 6. CI/CD

### plik. pullRequest.yml

```
name: Pull Request

on:
  pull_request:
    branches:
      - [ main ]
  workflow_dispatch:

jobs:
  test:
    runs-on: macos-13
    steps:
      - uses: actions/checkout@v2

      - name: Cancel Previous Runs
        uses: styfle/cancel-workflow-action@0.9.1
        with:
          access_token: ${{ github.token }}

      - uses: maxim-lobanov/setup-xcode@v1
        with:
          xcode-version: latest-stable

      - uses: ruby/setup-ruby@v1

      - name: Install Bundler
        run: gem install bundler

      - name: Install gems
        run: bundle install

      - name: Swift Packages Cache
        uses: actions/cache@v2
        id: cache
        with:
          path: |
            Build/SourcePackages
            Build/Build/Products
          key: ${{ runner.os }}-deps-v1-${{ hashFiles('BILDsolid.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved') }}
          restore-keys: ${{ runner.os }}-deps-v1-

      - name: Run Tests (No Cache)
        if: steps.setup.outputs.cache-hit != 'true'
        run: bundle exec fastlane unit_test
      
      - name: Run Tests (Cache)
        if: steps.setup.outputs.cache-hit == 'true'
        run: bundle exec fastlane unit_test skip_package_dependencies_resolution:true
```

### Screen z działania:
<img width="951" alt="Zrzut ekranu 2023-04-27 o 11 02 07" src="https://user-images.githubusercontent.com/77201172/234820791-366a6550-0a65-4974-9ebc-58da06ba7835.png">
<img width="913" alt="Zrzut ekranu 2023-04-27 o 10 38 16" src="https://user-images.githubusercontent.com/77201172/234820982-38bc7be3-f49d-48f6-951d-2a98111031a4.png">

