import { Helmet } from 'react-helmet-async'
import { useUser } from '@/store/auth.store'

const DashboardPage = () => {
  const { user, isAthlete, isCoach } = useUser()

  return (
    <>
      <Helmet>
        <title>Dashboard | BYD90</title>
        <meta name="description" content="Your BYD90 dashboard" />
      </Helmet>

      <div className="min-h-screen bg-gray-50">
        <div className="container py-8">
          <div className="max-w-4xl mx-auto">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-gray-900">
                Welcome back, {user?.first_name}!
              </h1>
              <p className="text-gray-600 mt-2">
                {isAthlete ? 'Track your performance and get AI recommendations' : 'Manage your athletes and training programs'}
              </p>
            </div>

            {/* Dashboard Content */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div className="card p-6">
                <h3 className="text-lg font-semibold mb-4">Quick Stats</h3>
                <div className="space-y-3">
                  <div className="flex justify-between">
                    <span className="text-gray-600">Workouts this week</span>
                    <span className="font-semibold">5</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Current streak</span>
                    <span className="font-semibold">12 days</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Level</span>
                    <span className="font-semibold">Advanced</span>
                  </div>
                </div>
              </div>

              <div className="card p-6">
                <h3 className="text-lg font-semibold mb-4">Recent Activity</h3>
                <div className="space-y-3">
                  <div className="text-sm">
                    <div className="font-medium">Strength Training</div>
                    <div className="text-gray-600">2 hours ago</div>
                  </div>
                  <div className="text-sm">
                    <div className="font-medium">Cardio Session</div>
                    <div className="text-gray-600">Yesterday</div>
                  </div>
                  <div className="text-sm">
                    <div className="font-medium">Skills Practice</div>
                    <div className="text-gray-600">2 days ago</div>
                  </div>
                </div>
              </div>

              <div className="card p-6">
                <h3 className="text-lg font-semibold mb-4">AI Recommendations</h3>
                <div className="space-y-3">
                  <div className="bg-primary-50 p-3 rounded-lg">
                    <div className="text-sm font-medium text-primary-800">
                      Focus on agility drills
                    </div>
                    <div className="text-xs text-primary-600 mt-1">
                      Confidence: 92%
                    </div>
                  </div>
                  <button className="btn btn-primary btn-sm w-full">
                    View All Recommendations
                  </button>
                </div>
              </div>
            </div>

            {/* Additional sections would go here */}
            <div className="mt-8 text-center">
              <p className="text-gray-600">
                🚧 Dashboard is under construction. More features coming soon!
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default DashboardPage
