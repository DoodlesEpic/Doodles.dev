# Doodles' website

<img alt="Doodles Logo" src="https://user-images.githubusercontent.com/37254797/169932071-59d0a264-1802-431e-8c46-da491c2e79ed.png" height="150px" class="avatar">

## About

Hello, my name is Eduardo, but you can call me Doodles! This is my little personal website with blog posts, projects, and contact information. This website was developed using Jekyll, and it's currently available at [doodlesdev.com](https://www.doodlesdev.com). 

If my domain ever goes down for some reason, since this is deployed from a Netlify free-tier account, it will still be accessible at [doodlesdev.netlify.app](https://doodlesdev.netlify.app).

## Performance considerations

This site intentionally inlines its theme CSS in the document head instead of linking to a standalone stylesheet. For a blog, the first page load is the most important path to optimize, because readers often arrive from search, RSS, social links, or direct links to individual posts. Inlining the small stylesheet avoids an extra render-blocking request on that first visit.

The tradeoff is that repeat navigation does not benefit from a cached stylesheet. That is acceptable for this site because first-load latency is the main goal. Since the inline CSS path no longer references `assets/css/style.css`, a small Jekyll plugin suppresses the theme's generated standalone stylesheet from the deployed output.

## Run locally

This project uses [mise](https://mise.jdx.dev/) to pin its local toolchain. To get started, install mise and the project's tools:

```bash
mise install
```

If mise is activated in your shell, it puts the pinned tools on your `PATH`, so you can run the usual commands directly from the project directory:

```bash
bundle install
```

Start the development server:

```bash
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000` in your browser to preview the website.

If mise is not activated in your shell, prefix commands with `mise exec --`, for example:

```bash
mise exec -- bundle install
mise exec -- bundle exec jekyll serve
```

You can also install Ruby, Python, Bundler, uv, and the other tools without mise. If you do, make sure your local versions match the versions pinned in `.mise.toml` and `Gemfile.lock`.

## Project data

Project listings are stored in `_data/projects.yml`. To refresh them from
GitHub, run the Python script documented in [`scripts/README.md`](scripts/README.md):

```bash
cd _data
uv --project ../scripts run python ../scripts/generate_projects.py
```

Run it from `_data` so the generated YAML updates the file used by Jekyll.

## License

### Content

This work © 2022-2026 by [Eduardo Moraes](https://github.com/DoodlesEpic/) is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

### Code

This project is licensed under the GNU AGPL v3.0 free software license. Read the [LICENSE](/LICENSE) file for more information.
