import { Helmet } from 'react-helmet-async'

const RecommendationsPage = () => {
  return (
    <>
      <Helmet>
        <title>Recommendations | BYD90</title>
      </Helmet>
      
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">AI Recommendations</h1>
          <p className="text-gray-600">🚧 Coming soon!</p>
        </div>
      </div>
    </>
  )
}
