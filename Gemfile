source "https://rubygems.org"
gem "jekyll", "~> 4.3.4"

# The minima theme to be used as gem
gem "doodles_minima", github: "DoodlesEpic/DoodlesMinima"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem 'jekyll-sitemap'
  gem 'jekyll-admin'
  gem 'jekyll-compose'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

