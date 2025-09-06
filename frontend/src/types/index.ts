// BYD90 TypeScript Type Definitions

// User Types
export type UserType = 'athlete' | 'coach' | 'admin'

export interface User {
  id: number
  email: string
  username: string
  first_name: string
  last_name: string
  user_type: UserType
  profile_picture?: string
  bio?: string
  phone_number?: string
  is_active: boolean
  is_verified: boolean
  is_premium: boolean
  created_at: string
  updated_at: string
  last_login?: string
  email_verified_at?: string
}

export interface UserCreate {
  email: string
  username: string
  password: string
  confirm_password: string
  first_name: string
  last_name: string
  user_type: UserType
  phone_number?: string
  terms_accepted: boolean
}

export interface UserLogin {
  email: string
  password: string
}

// Sport and Position Types
export type Sport = 
  | 'football' 
  | 'basketball' 
  | 'soccer' 
  | 'tennis' 
  | 'volleyball' 
  | 'baseball' 
  | 'hockey' 
  | 'swimming' 
  | 'track_field' 
  | 'golf'

export type AthletePosition = 
  // Football
  | 'quarterback' | 'running_back' | 'wide_receiver' | 'tight_end'
  | 'offensive_line' | 'defensive_line' | 'linebacker' | 'cornerback'
  | 'safety' | 'kicker' | 'punter'
  // Basketball
  | 'point_guard' | 'shooting_guard' | 'small_forward' | 'power_forward' | 'center'
  // Soccer
  | 'goalkeeper' | 'defender' | 'midfielder' | 'forward'
  // Tennis
  | 'singles' | 'doubles'
  // General
  | 'general'

// Athlete Types
export interface Athlete {
  id: number
  user_id: number
  primary_sport: Sport
  secondary_sports?: Sport[]
  primary_position: AthletePosition
  secondary_positions?: AthletePosition[]
  height?: number
  weight?: number
  date_of_birth?: string
  dominant_hand?: 'left' | 'right' | 'ambidextrous'
  experience_level?: 'beginner' | 'intermediate' | 'advanced' | 'professional'
  years_playing?: number
  current_team?: string
  jersey_number?: string
  fitness_metrics?: Record<string, any>
  skill_metrics?: Record<string, any>
  game_stats?: Record<string, any>
  training_goals?: string[]
  training_frequency?: number
  preferred_training_time?: 'morning' | 'afternoon' | 'evening'
  injury_history?: Record<string, any>
  current_injuries?: Record<string, any>
  recovery_status?: 'active' | 'recovering' | 'injured'
  privacy_settings?: Record<string, any>
  notification_preferences?: Record<string, any>
  created_at: string
  updated_at: string
}

// Coach Types
export type CoachLevel = 'youth' | 'high_school' | 'college' | 'professional' | 'recreational'

export type CoachSpecialization = 
  | 'general_coaching'
  | 'strength_conditioning'
  | 'skills_development'
  | 'mental_performance'
  | 'injury_prevention'
  | 'nutrition'
  | 'recovery'
  | 'youth_development'

export interface Coach {
  id: number
  user_id: number
  license_number?: string
  certifications?: string[]
  specializations?: CoachSpecialization[]
  coaching_level: CoachLevel
  years_coaching?: number
  sports_coached?: Sport[]
  current_organization?: string
  previous_organizations?: string[]
  coaching_philosophy?: string
  hourly_rate?: number
  availability?: Record<string, any>
  time_zone?: string
  average_rating: number
  total_reviews: number
  success_stories?: Record<string, any>
  accepts_new_athletes: boolean
  max_athletes?: number
  preferred_athlete_level?: string[]
  coaching_style?: string[]
  business_name?: string
  business_address?: string
  is_verified: boolean
  created_at: string
  updated_at: string
}

// Recommendation Types
export type RecommendationType = 
  | 'fitness'
  | 'skill_development'
  | 'recovery'
  | 'nutrition'
  | 'mental_performance'
  | 'injury_prevention'
  | 'equipment'
  | 'training_schedule'
  | 'goal_setting'

export type RecommendationPriority = 'low' | 'medium' | 'high' | 'urgent'
export type RecommendationStatus = 'pending' | 'in_progress' | 'completed' | 'dismissed' | 'expired'

export interface Recommendation {
  id: number
  athlete_id: number
  title: string
  description: string
  recommendation_type: RecommendationType
  priority: RecommendationPriority
  ai_model_version?: string
  confidence_score?: number
  reasoning?: string
  action_items?: Record<string, any>
  resources?: Record<string, any>
  metrics_to_track?: Record<string, any>
  based_on_factors?: Record<string, any>
  sport_specific: boolean
  position_specific: boolean
  estimated_duration?: number
  difficulty_level?: 'easy' | 'medium' | 'hard'
  required_equipment?: string[]
  status: RecommendationStatus
  implementation_notes?: string
  athlete_feedback?: Record<string, any>
  effectiveness_rating?: number
  measurable_improvement?: Record<string, any>
  scheduled_for?: string
  expires_at?: string
  completed_at?: string
  is_visible_to_coach: boolean
  coach_comments?: string
  created_at: string
  updated_at: string
}

// Community Types
export type CommunityType = 
  | 'sport_specific'
  | 'position_specific'
  | 'skill_level'
  | 'geographic'
  | 'team_based'
  | 'general'
  | 'training_group'

export type CommunityPrivacy = 'public' | 'private' | 'invite_only'

export interface Community {
  id: number
  name: string
  description?: string
  community_type: CommunityType
  privacy: CommunityPrivacy
  tags?: string[]
  rules?: Record<string, any>
  welcome_message?: string
  cover_image_url?: string
  icon_url?: string
  creator_id: number
  moderator_ids?: number[]
  is_moderated: boolean
  auto_approve_posts: boolean
  member_count: number
  post_count: number
  active_members_30d: number
  is_active: boolean
  is_featured: boolean
  created_at: string
  updated_at: string
  last_activity: string
}

export type PostType = 
  | 'text'
  | 'image'
  | 'video'
  | 'achievement'
  | 'workout'
  | 'progress'
  | 'question'
  | 'tip'
  | 'poll'

export interface Post {
  id: number
  community_id: number
  author_id: number
  title?: string
  content: string
  post_type: PostType
  media_urls?: string[]
  attachments?: Record<string, any>
  like_count: number
  comment_count: number
  share_count: number
  view_count: number
  is_approved: boolean
  is_pinned: boolean
  is_locked: boolean
  moderation_notes?: string
  tags?: string[]
  mentioned_users?: number[]
  created_at: string
  updated_at: string
}

export interface Comment {
  id: number
  post_id: number
  author_id: number
  parent_comment_id?: number
  content: string
  like_count: number
  reply_count: number
  is_approved: boolean
  moderation_notes?: string
  mentioned_users?: number[]
  created_at: string
  updated_at: string
}

// Avatar Types
export type AvatarStyle = 'realistic' | 'cartoon' | 'pixel_art' | 'minimalist' | 'sports_themed'
export type AvatarGender = 'male' | 'female' | 'non_binary' | 'custom'

export interface Avatar {
  id: number
  user_id: number
  name?: string
  style: AvatarStyle
  gender: AvatarGender
  physical_features?: Record<string, any>
  facial_features?: Record<string, any>
  hair?: Record<string, any>
  outfit?: Record<string, any>
  accessories?: Record<string, any>
  sports_gear?: Record<string, any>
  unlocked_items?: string[]
  purchased_items?: string[]
  earned_items?: string[]
  level: number
  experience_points: number
  achievements?: Record<string, any>
  is_public: boolean
  allow_customization_suggestions: boolean
  avatar_image_url?: string
  thumbnail_url?: string
  last_generated?: string
  created_at: string
  updated_at: string
}

// Auth Types
export interface AuthTokens {
  access_token: string
  refresh_token: string
  token_type: string
  expires_in: number
}

export interface LoginResponse extends AuthTokens {
  user: User
}

// API Response Types
export interface ApiResponse<T = any> {
  data?: T
  message?: string
  error?: string
  success: boolean
}

export interface PaginatedResponse<T = any> {
  data: T[]
  total: number
  page: number
  per_page: number
  total_pages: number
}

// Form Types
export interface FormField {
  name: string
  label: string
  type: 'text' | 'email' | 'password' | 'select' | 'textarea' | 'checkbox' | 'radio' | 'file'
  placeholder?: string
  required?: boolean
  options?: { value: string; label: string }[]
  validation?: Record<string, any>
}

// Component Props Types
export interface ComponentWithChildren {
  children: React.ReactNode
}

export interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  disabled?: boolean
  loading?: boolean
  type?: 'button' | 'submit' | 'reset'
  onClick?: () => void
  className?: string
  children: React.ReactNode
}

export interface ModalProps extends ComponentWithChildren {
  isOpen: boolean
  onClose: () => void
  title?: string
  size?: 'sm' | 'md' | 'lg' | 'xl'
}

// Navigation Types
export interface NavItem {
  name: string
  href: string
  icon?: React.ComponentType<any>
  current?: boolean
  badge?: string | number
  children?: NavItem[]
}

// Chart/Analytics Types
export interface ChartDataPoint {
  label: string
  value: number
  color?: string
}

export interface PerformanceMetric {
  name: string
  value: number
  unit?: string
  trend?: 'up' | 'down' | 'stable'
  change?: number
  target?: number
}
