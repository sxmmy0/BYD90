import axios from 'axios'
import { LoginResponse, UserCreate, AuthTokens } from '@/types'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

class AuthService {
  private baseURL = `${API_BASE_URL}/api/v1/auth`

  async login(email: string, password: string): Promise<LoginResponse> {
    const response = await axios.post(`${this.baseURL}/login/email`, {
      email,
      password,
    })
    return response.data
  }

  async register(userData: UserCreate): Promise<LoginResponse> {
    const response = await axios.post(`${this.baseURL}/register`, userData)
    return response.data
  }

  async refreshToken(refreshToken: string): Promise<AuthTokens> {
    const response = await axios.post(`${this.baseURL}/refresh`, {
      refresh_token: refreshToken,
    })
    return response.data
  }

  async logout(): Promise<void> {
    // In a real app, you might want to call the backend to invalidate the token
    await axios.post(`${this.baseURL}/logout`)
  }

  async getCurrentUser(token: string) {
    const response = await axios.get(`${this.baseURL}/me`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    return response.data
  }

  async requestPasswordReset(email: string): Promise<void> {
    const response = await axios.post(`${this.baseURL}/password-reset`, {
      email,
    })
    return response.data
  }

  async confirmPasswordReset(token: string, newPassword: string, confirmPassword: string): Promise<void> {
    const response = await axios.post(`${this.baseURL}/password-reset/confirm`, {
      token,
      new_password: newPassword,
      confirm_password: confirmPassword,
    })
    return response.data
  }

  async verifyEmail(token: string): Promise<void> {
    const response = await axios.post(`${this.baseURL}/verify-email`, {
      token,
    })
    return response.data
  }

  async resendVerificationEmail(token: string): Promise<void> {
    const response = await axios.post(`${this.baseURL}/resend-verification`, {}, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    return response.data
  }
}

export const authService = new AuthService()
