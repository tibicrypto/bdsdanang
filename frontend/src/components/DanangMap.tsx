// frontend/src/components/DanangMap.tsx
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

export default function DanangMap({ properties }) {
  const center: [number, number] = [16.0544, 108.2022] // Tọa độ trung tâm Đà Nẵng

  return (
    <MapContainer center={center} zoom={12} style={{ height: '600px', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; OpenStreetMap contributors'
      />
      
      {properties.map(prop => (
        <GeoJSON
          key={prop.id}
          data={prop.geojson}
          style={() => ({
            color: '#3388ff',
            weight: 2,
            opacity: 0.7
          })}
        />
      ))}
    </MapContainer>
  )
}
