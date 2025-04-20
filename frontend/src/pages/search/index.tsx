// frontend/src/pages/search/index.tsx
import dynamic from 'next/dynamic'
const DanangMap = dynamic(() => import('@/components/DanangMap'), { ssr: false })

export default function SearchPage() {
  const [results, setResults] = useState<Property[]>([])
  
  const handleSearch = async (filters: SearchFilters) => {
    const res = await fetch('/api/search', {
      method: 'POST',
      body: JSON.stringify(filters)
    })
    setResults(await res.json())
  }

  return (
    <div className="container">
      <SearchFilters onSubmit={handleSearch} />
      <DanangMap properties={results} />
      <PropertyList items={results} />
    </div>
  )
}
