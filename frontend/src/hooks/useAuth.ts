import { useAuthStore } from '@/store/auth.store'

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
