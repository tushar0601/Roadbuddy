/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useCallback } from "react";
import type { Vehicle, Notification } from "@/lib/types";
import { apiJson } from "@/lib/api";
import { Button } from "@/components/ui/button";
import { VehiclesCard } from "@/components/dashboard/vehiclesCard";
import { NotificationsCard } from "@/components/dashboard/notificationsCard";
import { AddVehicleDialog } from "@/components/dashboard/addVehicleDialog";
import { useAuth } from "@/lib/auth";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import { AuthGuard } from "@/components/auth/AuthGuard";
import { useNotificationsPolling } from "@/hooks/useNotificationsPolling";
import { ProfileMenu } from "@/components/dashboard/profileMenu";

export default function DashboardPage() {
  const { token, signOut } = useAuth();
  const router = useRouter();

  const [vehicles, setVehicles] = useState<Vehicle[]>([]);
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [openAdd, setOpenAdd] = useState(false);

  useEffect(() => {
    if (!token) router.push("/signin");
  }, [token, router]);

  const handleNotifError = useCallback(
    (e: any) => {
      const msg = e?.message || "";
      if (msg.includes("401")) signOut();
    },
    [signOut],
  );

  const { tick: fetchNotificationsOnce } = useNotificationsPolling({
    enabled: !!token,
    intervalMs: 12000,
    onData: setNotifications,
    onError: handleNotifError,
  });

  const fetchVehiclesOnce = useCallback(async () => {
    try {
      const v = await apiJson<Vehicle[]>("/vehicles");
      setVehicles(v);
    } catch (e: any) {
      const msg = e?.message || "Failed to load vehicles";
      if (msg.includes("401")) signOut();
      toast.error(msg);
    }
  }, [signOut]);

  useEffect(() => {
    if (!token) return;

    void (async () => {
      await fetchVehiclesOnce();
      await fetchNotificationsOnce();
    })();
  }, [token, fetchVehiclesOnce, fetchNotificationsOnce]);

  const refresh = useCallback(async () => {
    await Promise.all([fetchVehiclesOnce(), fetchNotificationsOnce()]);
  }, [fetchVehiclesOnce, fetchNotificationsOnce]);

  return (
    <AuthGuard>
      <div className="p-6 max-w-6xl mx-auto space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-semibold">RoadBuddy</h1>
            <p className="text-sm text-muted-foreground">
              Your vehicles & notifications
            </p>
          </div>

          <div className="flex gap-2 items-center">
            <Button variant="outline" onClick={refresh}>
              Refresh
            </Button>
            <Button onClick={() => setOpenAdd(true)}>Add vehicle</Button>
            <ProfileMenu />
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <VehiclesCard vehicles={vehicles} />
          <NotificationsCard notifications={notifications} />
        </div>

        <AddVehicleDialog
          open={openAdd}
          onOpenChange={setOpenAdd}
          onCreated={(newVehicle) =>
            setVehicles((prev) => [newVehicle, ...prev])
          }
        />
      </div>
    </AuthGuard>
  );
}
