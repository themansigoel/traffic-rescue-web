# Traffic Rescue website

Local static website for Traffic Rescue. No framework, package installation, tracking scripts, database or build step is required. Serve with `python3 -m http.server 8085 --bind 127.0.0.1` and open http://127.0.0.1:8085/.

Pages: index.html, support.html, privacy.html, contact.html and 404.html. App artwork is copied from the app repository; source provenance remains in that project. Site assets use system fonts and run without third-party font requests.

## Local-only and publication

The user requested local-only creation. Git push is source synchronization, not deployment. No GitHub Pages activation, Site registration or public App Store URLs are created. site-config.json records no live base URL. Before publishing, run `python3 configure_public_url.py https://YOUR-PUBLIC-BASE/` to emit canonical URLs, OG URLs/image, sitemap and robots, then verify the deployed support/privacy pages before entering them in App Store Connect. Do not use localhost or a proposed URL in App Store metadata. robots.txt is effective only at a host root; GitHub project sites must also check the account-root robots policy.

## Contact

FormSubmit endpoint: themansigoel@gmail.com. Forms use native POST, required fields, privacy acknowledgement, honeypot and FormSubmit's default CAPTCHA. After the first real submission, the inbox owner must activate FormSubmit using its email. No test messages were sent; delivery is unverified. FormSubmit's own confirmation page is used until a published custom thank-you URL is available. Do not claim success before the provider accepts submission. No secrets or API key are needed.

## SEO / generative-engine discoverability

Unique titles/descriptions, semantic headings, internal support links, mobile layout, MobileApplication and visible-content FAQ schema, Open Graph metadata, llms.txt, and configurable absolute sitemap/canonicals. No fabricated ratings, reviews, pricing, downloads or availability. Structured data does not guarantee a search enhancement or AI citation. Six app languages are mentioned as app capabilities; website copy is English and has no misleading hreflang translations.

Run `python3 verify_site.py` for local link/image checks, JSON-LD parsing, headings and contact configuration. Native form delivery, public crawlability, App Store availability and policy/disclosure alignment need verification after hosting.

## Published status update

GitHub Pages was verified live on 12 October 2026 at https://themansigoel.github.io/traffic-rescue-web/. Support, privacy and contact pages returned HTTP 200. Canonical, OG and sitemap metadata now use the verified base URL. Earlier local-only notes describe initial creation. FormSubmit inbox activation/delivery remains unverified.
