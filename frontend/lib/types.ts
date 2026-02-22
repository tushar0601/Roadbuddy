/* eslint-disable @typescript-eslint/no-explicit-any */
export type AuthResponse = { access_token: string; token_type?: string };

export type Vehicle = {
  id: string;
  label: string;
  plate_last4?: string | null;
};

export type Notification = {
  id: string;
  vehicle_id: string;
  title: string;
  body: string;
  is_read: boolean;
  created_at: string;
  data?: Record<string, any>;
};

export type Sticker = {
  id: string;
  vehicle_id: string;
  public_code: string;
  status: "ACTIVE" | "REVOKED" | string;
  created_at?: string;
};
