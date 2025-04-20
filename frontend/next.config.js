// frontend/next.config.js
module.exports = {
  reactStrictMode: true,
  images: {
    domains: ['cdn.danangbds.com', 'batdongsan.com.vn'],
  },
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: process.env.NEXT_PUBLIC_API_URL + '/:path*'
      }
    ]
  }
}
