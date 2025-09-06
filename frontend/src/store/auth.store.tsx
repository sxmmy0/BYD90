import React from 'react'
import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { User, AuthTokens, LoginResponse } from '@/types'
import { authService } from '@/services/auth.service'
import toast from 'react-hot-toast'

interface AuthState {
  user: User | null
  tokens: AuthTokens | null
  isAuthenticated: boolean
  isLoading: boolean
  error: string | null
}

interface AuthActions {
  login: (email: string, password: string) => Promise<void>
  register: (userData: any) => Promise<void>
  logout: () => void
  refreshToken: () => Promise<void>
  updateUser: (userData: Partial<User>) => void
  clearError: () => void
  setLoading: (loading: boolean) => void
}

type AuthStore = AuthState & AuthActions

export const useAuthStore = create<AuthStore>()(
  persist(
    (set, get) => ({
      // Initial State
      user: null,
      tokens: null,
      isAuthenticated: false,
      isLoading: false,
      error: null,

      // Actions
      login: async (email: string, password: string) => {
        set({ isLoading: true, error: null })
        
        try {
          const response: LoginResponse = await authService.login(email, password)
          
          set({
            user: response.user,
            tokens: {
              access_token: response.access_token,
              refresh_token: response.refresh_token,
              token_type: response.token_type,
              expires_in: response.expires_in,
            },
            isAuthenticated: true,
            isLoading: false,
            error: null,
          })

          toast.success(`Welcome back, ${response.user.first_name}!`)
        } catch (error: any) {
          const errorMessage = error.response?.data?.detail || 'Login failed'
          set({ 
            error: errorMessage, 
            isLoading: false,
            isAuthenticated: false,
            user: null,
            tokens: null,
          })
          toast.error(errorMessage)
          throw error
        }
      },

      register: async (userData: any) => {
        set({ isLoading: true, error: null })
        
        try {
          const response: LoginResponse = await authService.register(userData)
          
          set({
            user: response.user,
            tokens: {
              access_token: response.access_token,
              refresh_token: response.refresh_token,
              token_type: response.token_type,
              expires_in: response.expires_in,
            },
            isAuthenticated: true,
            isLoading: false,
            error: null,
          })

          toast.success(`Welcome to BYD90, ${response.user.first_name}!`)
        } catch (error: any) {
          const errorMessage = error.response?.data?.detail || 'Registration failed'
          set({ 
            error: errorMessage, 
            isLoading: false,
            isAuthenticated: false,
            user: null,
            tokens: null,
          })
          toast.error(errorMessage)
          throw error
        }
      },

      logout: () => {
        set({
          user: null,
          tokens: null,
          isAuthenticated: false,
          error: null,
        })
        toast.success('Logged out successfully')
      },

      refreshToken: async () => {
        const { tokens } = get()
        
        if (!tokens?.refresh_token) {
          throw new Error('No refresh token available')
        }

        try {
          const response = await authService.refreshToken(tokens.refresh_token)
          
          set({
            tokens: {
              access_token: response.access_token,
              refresh_token: response.refresh_token,
              token_type: response.token_type,
              expires_in: response.expires_in,
            },
          })
        } catch (error) {
          // If refresh fails, logout user
          get().logout()
          throw error
        }
      },

      updateUser: (userData: Partial<User>) => {
        const { user } = get()
        if (user) {
          set({
            user: { ...user, ...userData }
          })
        }
      },

      clearError: () => {
        set({ error: null })
      },

      setLoading: (loading: boolean) => {
        set({ isLoading: loading })
      },
    }),
    {
      name: 'byd90-auth',
      partialize: (state) => ({
        user: state.user,
        tokens: state.tokens,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
)

// Auth Provider component for initialization
export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { user, tokens, refreshToken, logout } = useAuthStore()

  // Check if token is expired and refresh if needed
  React.useEffect(() => {
    if (tokens?.access_token && user) {
      // Decode JWT to check expiration (simplified)
      try {
        const payload = JSON.parse(atob(tokens.access_token.split('.')[1]))
        const currentTime = Date.now() / 1000
        
        // If token expires in less than 5 minutes, refresh it
        if (payload.exp - currentTime < 300) {
          refreshToken().catch(() => {
            logout()
          })
        }
      } catch (error) {
        console.error('Error parsing token:', error)
        logout()
      }
    }
  }, [tokens, user, refreshToken, logout])

  return <>{children}</>
}

// Helper hooks
export const useAuth = () => {
  const store = useAuthStore()
  return {
    user: store.user,
    tokens: store.tokens,
    isAuthenticated: store.isAuthenticated,
    isLoading: store.isLoading,
    error: store.error,
    login: store.login,
    register: store.register,
    logout: store.logout,
    refreshToken: store.refreshToken,
    updateUser: store.updateUser,
    clearError: store.clearError,
  }
}

export const useUser = () => {
  const user = useAuthStore((state) => state.user)
  const updateUser = useAuthStore((state) => state.updateUser)
  
  return {
    user,
    updateUser,
    isAthlete: user?.user_type === 'athlete',
    isCoach: user?.user_type === 'coach',
    isAdmin: user?.user_type === 'admin',
    isVerified: user?.is_verified ?? false,
    isPremium: user?.is_premium ?? false,
  }
}
