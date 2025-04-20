// frontend/src/components/SearchFilters.tsx
import { useState } from 'react'

export default function SearchFilters({ onSubmit }) {
  const [filters, setFilters] = useState({
    minPrice: 1,
    maxPrice: 20,
    districts: ['Hải Châu', 'Sơn Trà'],
    propertyType: 'all'
  })

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit(filters)
  }

  return (
    <form onSubmit={handleSubmit} className="search-filters">
      <div className="price-range">
        <label>Khoảng giá (tỷ VND)</label>
        <input type="range" min="1" max="100" 
          value={filters.maxPrice} 
          onChange={e => setFilters({...filters, maxPrice: e.target.value})}
        />
      </div>
      
      <button type="submit">Tìm kiếm</button>
    </form>
  )
}
