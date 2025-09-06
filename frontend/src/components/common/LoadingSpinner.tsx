import { clsx } from 'clsx'

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'large'
  className?: string
  color?: 'primary' | 'white' | 'gray'
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({ 
  size = 'md', 
  className,
  color = 'primary'
}) => {
  const sizeClasses = {
    sm: 'h-4 w-4',
    md: 'h-8 w-8',
    large: 'h-12 w-12'
  }

  const colorClasses = {
    primary: 'border-primary-600',
    white: 'border-white',
    gray: 'border-gray-600'
  }

  return (
    <div
      className={clsx(
        'spinner',
        sizeClasses[size],
        colorClasses[color],
        className
      )}
      aria-label="Loading"
    />
  )
}

export default LoadingSpinner
