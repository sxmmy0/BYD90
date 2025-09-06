import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Helmet } from 'react-helmet-async'
import { 
  Users, 
  TrendingUp, 
  Target, 
  Brain, 
  Award,
  ChevronRight,
  Play,
  Check
} from 'lucide-react'

const LandingPage = () => {
  const features = [
    {
      icon: Brain,
      title: 'AI-Powered Recommendations',
      description: 'Get personalized training suggestions based on your sport, position, and performance data.'
    },
    {
      icon: Users,
      title: 'Coach-Athlete Connection',
      description: 'Connect with certified coaches and build meaningful training relationships.'
    },
    {
      icon: TrendingUp,
      title: 'Performance Tracking',
      description: 'Monitor your progress with detailed analytics and insights.'
    },
    {
      icon: Target,
      title: 'Position-Specific Training',
      description: 'Tailored workouts and drills for your specific position and sport.'
    },
    {
      icon: Award,
      title: 'Achievement System',
      description: 'Unlock badges and rewards as you reach your fitness goals.'
    },
    {
      icon: Users,
      title: 'Community Support',
      description: 'Join communities of athletes and share your journey.'
    }
  ]

  const stats = [
    { number: '10K+', label: 'Athletes' },
    { number: '500+', label: 'Coaches' },
    { number: '50+', label: 'Sports' },
    { number: '95%', label: 'Success Rate' }
  ]

  return (
    <>
      <Helmet>
        <title>BYD90 - Beyond Ninety | AI-Powered Athlete Performance Platform</title>
        <meta name="description" content="Join thousands of athletes using AI-powered recommendations to improve performance, connect with coaches, and achieve their goals." />
      </Helmet>

      <div className="min-h-screen bg-white">
        {/* Navigation */}
        <nav className="bg-white shadow-sm border-b border-gray-200">
          <div className="container">
            <div className="flex justify-between items-center py-4">
              <div className="flex items-center space-x-2">
                <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold text-sm">B90</span>
                </div>
                <span className="text-xl font-bold text-gray-900">BYD90</span>
              </div>
              
              <div className="hidden md:flex items-center space-x-8">
                <a href="#features" className="nav-link">Features</a>
                <a href="#how-it-works" className="nav-link">How it Works</a>
                <a href="#pricing" className="nav-link">Pricing</a>
                <a href="#about" className="nav-link">About</a>
              </div>

              <div className="flex items-center space-x-4">
                <Link to="/login" className="btn btn-ghost btn-sm">
                  Sign In
                </Link>
                <Link to="/register" className="btn btn-primary btn-sm">
                  Get Started
                </Link>
              </div>
            </div>
          </div>
        </nav>

        {/* Hero Section */}
        <section className="section bg-gradient-to-br from-primary-50 via-white to-secondary-50">
          <div className="container">
            <div className="grid lg:grid-cols-2 gap-12 items-center">
              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 mb-6">
                  Beyond Ninety.{' '}
                  <span className="text-gradient">
                    Beyond Limits.
                  </span>
                </h1>
                <p className="text-xl text-gray-600 mb-8 leading-relaxed">
                  AI-powered athlete performance platform that connects athletes with coaches, 
                  provides personalized training recommendations, and helps you achieve your goals.
                </p>
                <div className="flex flex-col sm:flex-row gap-4">
                  <Link to="/register" className="btn btn-primary btn-lg">
                    Start Your Journey
                    <ChevronRight className="ml-2 h-5 w-5" />
                  </Link>
                  <button className="btn btn-outline btn-lg group">
                    <Play className="mr-2 h-5 w-5 group-hover:scale-110 transition-transform" />
                    Watch Demo
                  </button>
                </div>
              </motion.div>

              <motion.div
                initial={{ opacity: 0, x: 30 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.6, delay: 0.2 }}
                className="relative"
              >
                <div className="bg-white rounded-2xl shadow-large p-8">
                  <div className="space-y-6">
                    <div className="flex items-center space-x-4">
                      <div className="avatar avatar-lg">
                        <div className="w-12 h-12 bg-gradient-primary rounded-full flex items-center justify-center">
                          <Users className="h-6 w-6 text-white" />
                        </div>
                      </div>
                      <div>
                        <h3 className="font-semibold text-gray-900">Alex Rodriguez</h3>
                        <p className="text-gray-600">Basketball Point Guard</p>
                      </div>
                      <div className="ml-auto badge badge-success">Active</div>
                    </div>
                    
                    <div className="bg-gray-50 rounded-lg p-4">
                      <h4 className="font-medium text-gray-900 mb-2">Today's AI Recommendation</h4>
                      <p className="text-sm text-gray-600">
                        Focus on ball handling drills for 20 minutes, followed by 3-point shooting practice.
                      </p>
                      <div className="mt-3 flex items-center text-sm text-primary-600">
                        <Check className="h-4 w-4 mr-1" />
                        Confidence: 94%
                      </div>
                    </div>
                    
                    <div className="grid grid-cols-3 gap-4 text-center">
                      <div>
                        <div className="text-2xl font-bold text-gray-900">85%</div>
                        <div className="text-sm text-gray-600">Accuracy</div>
                      </div>
                      <div>
                        <div className="text-2xl font-bold text-gray-900">12</div>
                        <div className="text-sm text-gray-600">Workouts</div>
                      </div>
                      <div>
                        <div className="text-2xl font-bold text-gray-900">Level 5</div>
                        <div className="text-sm text-gray-600">Progress</div>
                      </div>
                    </div>
                  </div>
                </div>
              </motion.div>
            </div>
          </div>
        </section>

        {/* Stats Section */}
        <section className="py-16 bg-gray-900">
          <div className="container">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
              {stats.map((stat, index) => (
                <motion.div
                  key={stat.label}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                  className="text-center"
                >
                  <div className="text-3xl md:text-4xl font-bold text-white mb-2">
                    {stat.number}
                  </div>
                  <div className="text-gray-400">{stat.label}</div>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="section">
          <div className="container">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                Everything You Need to Excel
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                Comprehensive tools and features designed to help athletes and coaches 
                achieve peak performance and build stronger connections.
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
              {features.map((feature, index) => (
                <motion.div
                  key={feature.title}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                  className="card card-hover p-6"
                >
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                    <feature.icon className="h-6 w-6 text-primary-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-3">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600">
                    {feature.description}
                  </p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="section bg-gradient-primary">
          <div className="container text-center">
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
            >
              <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
                Ready to Transform Your Athletic Journey?
              </h2>
              <p className="text-xl text-primary-100 mb-8 max-w-2xl mx-auto">
                Join thousands of athletes and coaches who are already using BYD90 
                to achieve their goals and push beyond their limits.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Link to="/register" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                  Get Started Free
                </Link>
                <Link to="/login" className="btn border-white text-white hover:bg-white hover:text-primary-600 btn-lg">
                  Sign In
                </Link>
              </div>
            </motion.div>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-gray-900 text-white py-12">
          <div className="container">
            <div className="grid md:grid-cols-4 gap-8">
              <div>
                <div className="flex items-center space-x-2 mb-4">
                  <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center">
                    <span className="text-white font-bold text-sm">B90</span>
                  </div>
                  <span className="text-xl font-bold">BYD90</span>
                </div>
                <p className="text-gray-400">
                  Empowering athletes to go beyond ninety and achieve their full potential.
                </p>
              </div>
              
              <div>
                <h4 className="font-semibold mb-4">Platform</h4>
                <ul className="space-y-2 text-gray-400">
                  <li><a href="#" className="hover:text-white transition-colors">Features</a></li>
                  <li><a href="#" className="hover:text-white transition-colors">Pricing</a></li>
                  <li><a href="#" className="hover:text-white transition-colors">API</a></li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-4">Support</h4>
                <ul className="space-y-2 text-gray-400">
                  <li><a href="#" className="hover:text-white transition-colors">Help Center</a></li>
                  <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
                  <li><a href="#" className="hover:text-white transition-colors">Community</a></li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-4">Company</h4>
                <ul className="space-y-2 text-gray-400">
                  <li><a href="#" className="hover:text-white transition-colors">About</a></li>
                  <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
                  <li><a href="#" className="hover:text-white transition-colors">Careers</a></li>
                </ul>
              </div>
            </div>
            
            <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
              <p>&copy; 2024 BYD90. All rights reserved.</p>
            </div>
          </div>
        </footer>
      </div>
    </>
  )
}

export default LandingPage
