"use client";

import React, {
  createContext,
  useContext,
  useMemo,
  useState,
  useCallback,
} from "react";
import { useRouter } from "next/navigation";
import { tokenStore } from "./storage";

type AuthCtx = {
  token: string | null;
  setToken: (t: string | null) => void;
  signOut: () => void;
};

const Ctx = createContext<AuthCtx | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const router = useRouter();

  const [token, setTokenState] = useState<string | null>(() =>
    tokenStore.get(),
  );

  const setToken = useCallback((t: string | null) => {
    setTokenState(t);
    if (t) tokenStore.set(t);
    else tokenStore.clear();
  }, []);

  const signOut = useCallback(() => {
    setToken(null);
    router.push("/signin");
  }, [router, setToken]);

  const value = useMemo(
    () => ({ token, setToken, signOut }),
    [token, setToken, signOut],
  );

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useAuth() {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
