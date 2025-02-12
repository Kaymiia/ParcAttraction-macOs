export interface CritiqueInterface {
  critique_id: number | null,
  attraction_id: number | null,
  nom: string | null,
  prenom: string | null,
  texte: string,
  note: number
}