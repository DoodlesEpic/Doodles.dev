# frozen_string_literal: true

Jekyll::Hooks.register :site, :post_read do |site|
  # The theme's stylesheet is inlined from _includes/head.html, so skip the
  # unreferenced standalone CSS file in the generated site.
  site.pages.reject! { |page| page.relative_path == "assets/css/style.scss" }
end
